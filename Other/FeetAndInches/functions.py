
def convert_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 0.0254

if __name__ == "__main__":
    print(convert_to_meters(5, 11))