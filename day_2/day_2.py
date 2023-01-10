def main():
    box_dimension_list = []
    square_feet_wrapping_paper_needed = 0
    feet_ribbon_needed = 0
    
    # Read and store all dimensions in 2d list
    with open("inputs/day_2.txt") as f:
        for line in f:
            box_dimension_list.append(line.strip().split("x"))

    # Sum up the square footage needed for each box
    for l,w,h in box_dimension_list:
        l = int(l)
        w = int(w)
        h = int(h)

        lw = l*w
        wh = w*h
        hl = h*l

        square_feet_wrapping_paper_needed += 2*lw + 2*wh + 2*hl + min(lw, wh, hl)
        feet_ribbon_needed += 2*(l+w+h) - 2*max(l,w,h) + l*w*h

    print(f"Square footage needed: {square_feet_wrapping_paper_needed}")
    print(f"Feet of ribbon needed: {feet_ribbon_needed}")

if __name__ == "__main__":
    main()
