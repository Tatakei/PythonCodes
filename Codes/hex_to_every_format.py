import colorsys
import math

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    return (red, green, blue)

def rgb_to_hsv(red, green, blue):
    red, green, blue = red / 255.0, green / 255.0, blue / 255.0
    hue, saturation, value = colorsys.rgb_to_hsv(red, green, blue)
    hue = hue * 360
    saturation = saturation * 100
    value = value * 100
    return (hue, saturation, value)

def rgb_to_hsl(red, green, blue):
    red, green, blue = red / 255.0, green / 255.0, blue / 255.0
    hue, saturation, lightness = colorsys.rgb_to_hls(red, green, blue)
    hue = hue * 360
    saturation = saturation * 100
    lightness = lightness * 100
    return (hue, saturation, lightness)

def rgb_to_cmy(red, green, blue):
    cyan = 1 - (red / 255.0)
    magenta = 1 - (green / 255.0)
    yellow = 1 - (blue / 255.0)
    return (cyan * 100, magenta * 100, yellow * 100)

def rgb_to_cmyk(red, green, blue):
    c, m, y = rgb_to_cmy(red, green, blue)
    k = min(c, m, y) / 100  # Calculate Black Key
    if k == 1:
        c, m, y = 0, 0, 0
    else:
        c = (c - k) / (1 - k) * 100
        m = (m - k) / (1 - k) * 100
        y = (y - k) / (1 - k) * 100
    return (c, m, y, k * 100)

def rgb_to_xyz(red, green, blue):
    # Convert RGB to XYZ color space
    r = red / 255.0
    g = green / 255.0
    b = blue / 255.0
    
    # Apply the transformation
    r = r / 12.92 if r <= 0.04045 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.04045 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.04045 else ((b + 0.055) / 1.055) ** 2.4
    
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    return (x * 100, y * 100, z * 100)

def rgb_to_lab(red, green, blue):
    # Convert RGB to XYZ
    xyz = rgb_to_xyz(red, green, blue)
    
    # Convert XYZ to Lab
    x, y, z = xyz
    x = x / 95.047  # Reference white
    y = y / 100.000
    z = z / 108.883

    x = x ** (1/3) if x > 0.008856 else (x * 7.787 + 16 / 116)
    y = y ** (1/3) if y > 0.008856 else (y * 7.787 + 16 / 116)
    z = z ** (1/3) if z > 0.008856 else (z * 7.787 + 16 / 116)

    l = max(0, min(100, (116 * y - 16)))
    a = (x - y) * 500
    b = (y - z) * 200

    return (l, a, b)

def rgb_to_lch(red, green, blue):
    lab = rgb_to_lab(red, green, blue)
    l, a, b = lab
    c = (a ** 2 + b ** 2) ** 0.5
    h = (180 / math.pi) * (math.atan2(b, a) % (2 * math.pi))
    return (l, c, h)

def rgb_to_yuv(red, green, blue):
    y = 0.299 * red + 0.587 * green + 0.114 * blue
    u = -0.14713 * red - 0.28886 * green + 0.436 * blue
    v = 0.615 * red - 0.51498 * green - 0.10001 * blue
    return (y, u, v)

def rgb_to_ycbcr(red, green, blue):
    y = 0.299 * red + 0.587 * green + 0.114 * blue
    cb = (blue - y) * 0.564 + 128
    cr = (red - y) * 0.713 + 128
    return (y, cb, cr)

def rgb_to_hex(red, green, blue):
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)

def rgb_to_css_rgb(red, green, blue):
    return f"rgb({red}, {green}, {blue})"

def rgb_to_css_rgba(red, green, blue, alpha=1.0):
    return f"rgba({red}, {green}, {blue}, {alpha})"

def rgb_to_percentage(red, green, blue):
    return (red / 255.0 * 100, green / 255.0 * 100, blue / 255.0 * 100)

def rgb_to_grayscale(red, green, blue):
    return (red + green + blue) // 3

def get_complementary_color(red, green, blue):
    return (255 - red, 255 - green, 255 - blue)

def get_triadic_colors(red, green, blue):
    return [
        (red, green, blue),
        ((red + 120) % 360, (green + 120) % 360, (blue + 120) % 360),
        ((red + 240) % 360, (green + 240) % 360, (blue + 240) % 360),
    ]

def get_tetradic_colors(red, green, blue):
    return [
        (red, green, blue),
        (green, blue, red),
        (blue, red, green),
        (red, green, blue),  # repeat original
    ]

# Main logic
if __name__ == "__main__":
    hex_color = input("\033[31mEnter a hex color code (e.g., #FF5733): \033[0m")  # Red text for prompt

    try:
        rgb_color = hex_to_rgb(hex_color)
        print(f"\033[33mThe RGB color is: {rgb_color}\033[0m")  # Blue text

        hsv_color = rgb_to_hsv(*rgb_color)
        print(f"\033[33mThe HSV color is: Hue = {hsv_color[0]:.2f}°, Saturation = {hsv_color[1]:.2f}%, Value = {hsv_color[2]:.2f}%\033[0m")  # Blue text

        hsl_color = rgb_to_hsl(*rgb_color)
        print(f"\033[33mThe HSL color is: Hue = {hsl_color[0]:.2f}°, Saturation = {hsl_color[1]:.2f}%, Lightness = {hsl_color[2]:.2f}%\033[0m")  # Blue text

        cmy_color = rgb_to_cmy(*rgb_color)
        print(f"\033[34mThe CMY color is: Cyan = {cmy_color[0]:.2f}%, Magenta = {cmy_color[1]:.2f}%, Yellow = {cmy_color[2]:.2f}%\033[0m")  # Blue text

        cmyk_color = rgb_to_cmyk(*rgb_color)
        print(f"\033[32mThe CMYK color is: Cyan = {cmyk_color[0]:.2f}%, Magenta = {cmyk_color[1]:.2f}%, Yellow = {cmyk_color[2]:.2f}%, Black = {cmyk_color[3]:.2f}%\033[0m")  # Blue text

        xyz_color = rgb_to_xyz(*rgb_color)
        print(f"\033[34mThe XYZ color is: X = {xyz_color[0]:.2f}, Y = {xyz_color[1]:.2f}, Z = {xyz_color[2]:.2f}\033[0m")  # Blue text

        lab_color = rgb_to_lab(*rgb_color)
        print(f"\033[32mThe Lab color is: L = {lab_color[0]:.2f}, a = {lab_color[1]:.2f}, b = {lab_color[2]:.2f}\033[0m")  # Blue text

        lch_color = rgb_to_lch(*rgb_color)
        print(f"\033[34mThe LCH color is: L = {lch_color[0]:.2f}, C = {lch_color[1]:.2f}, H = {lch_color[2]:.2f}°\033[0m")  # Blue text

        yuv_color = rgb_to_yuv(*rgb_color)
        print(f"\033[32mThe YUV color is: Y = {yuv_color[0]:.2f}, U = {yuv_color[1]:.2f}, V = {yuv_color[2]:.2f}\033[0m")  # Blue text

        ycbcr_color = rgb_to_ycbcr(*rgb_color)
        print(f"\033[34mThe YCbCr color is: Y = {ycbcr_color[0]:.2f}, Cb = {ycbcr_color[1]:.2f}, Cr = {ycbcr_color[2]:.2f}\033[0m")  # Blue text

        hex_color = rgb_to_hex(*rgb_color)
        print(f"\033[32mThe HEX color code is: {hex_color}\033[0m")  # Blue text

        css_rgb = rgb_to_css_rgb(*rgb_color)
        print(f"\033[34mThe CSS RGB format is: {css_rgb}\033[0m")  # Blue text

        css_rgba = rgb_to_css_rgba(*rgb_color)
        print(f"\033[32mThe CSS RGBA format (with alpha 1.0) is: {css_rgba}\033[0m")  # Blue text

        percentage = rgb_to_percentage(*rgb_color)
        print(f"\033[34mThe percentage values are: R = {percentage[0]:.2f}%, G = {percentage[1]:.2f}%, B = {percentage[2]:.2f}%\033[0m")  # Blue text

        grayscale = rgb_to_grayscale(*rgb_color)
        print(f"\033[32mThe Grayscale value is: {grayscale}\033[0m")  # Blue text

        complementary_color = get_complementary_color(*rgb_color)
        print(f"\033[34mThe Complementary color (RGB) is: {complementary_color}\033[0m")  # Blue text

        triadic_colors = get_triadic_colors(*rgb_color)
        print(f"\033[32mThe Triadic colors (RGB) are: {triadic_colors}\033[0m")  # Blue text

        tetradic_colors = get_tetradic_colors(*rgb_color)
        print(f"\033[34mThe Tetradic colors (RGB) are: {tetradic_colors}\033[0m")  # Blue text

    except ValueError:
        print("\033[31mInvalid HEX color code! Please enter a valid HEX color code (e.g., #FF5733).\033[0m")  # Red text
