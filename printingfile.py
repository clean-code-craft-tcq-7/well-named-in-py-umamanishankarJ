from colour_calc import get_color_from_pair_number
from telecom_colour import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def print_color_code_manual():
    manual_lines = []
    manual_lines.append("Pair No. | Major Color | Minor Color")
    manual_lines.append("-----------------------------------")
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual_lines.append(f"{pair_number:<8} | {major_color:<11} | {minor_color}")
    return "\n".join(manual_lines)
