#!/usr/bin/python3
"""
module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    each box is numbered sequentially from 0 to n- 1,
    and each box may contain keys to the other boxes.
    Determine if all the boxes can be opened.
    """
    if boxes is None:
        return False 
    if len(boxes) == 1:
        return True
    #Track the visited boxes
    visited = set()
    #the first box is unlocked!!
    visited.add(0)

    #use a stack to do a depth irst Search
    stack = []
    stack.append(0)

    while stack:
        keys = boxes[stack.pop()]
        for key in keys:
            if key not in visited:
                visited.add(key)
                stack.append(key)
            #All have been visited if the 
            #number of boxes is equal to the 
            #number of visited boxes  ends
            return len(boxes) == len(visited)
