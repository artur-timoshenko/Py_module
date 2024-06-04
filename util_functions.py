from structures import dot,angle,line

def are_parallel(line1, line2):
    slope1 = (line1.end.y - line1.start.y) / (line1.end.x - line1.start.x) if line1.end.x != line1.start.x else float('inf')
    slope2 = (line2.end.y - line2.start.y) / (line2.end.x - line2.start.x) if line2.end.x != line2.start.x else float('inf')
    
    return slope1 == slope2