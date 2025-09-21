def printf(s):
    print("".join(s)[2: -2])

def fix(s):
    while True:
        has_empty = False
        is_changed = False
        for i in range(2, n + 2):
            if s[i] == "0":
                is_left_forced = False
                if s[i - 1] == "1" and s[i - 2] == "R":
                    is_left_forced = True
                has_left_option = True
                if s[i - 1] == "1" and s[i - 2] in "B1L":
                    has_left_option = False

                is_right_forced = False
                if s[i + 1] == "1" and s[i + 2] == "L":
                    is_right_forced = True
                has_right_option = True
                if s[i + 1] == "1" and s[i + 2] in "B1R":
                    has_right_option = False
                
                if is_left_forced and is_right_forced:
                    return False
                elif is_left_forced:
                    s[i] = "L"
                    is_changed = True
                elif is_right_forced:
                    s[i] = "R"
                    is_changed = True
                # At this point, nothing is forced
                elif has_left_option and has_right_option:
                    has_empty = True
                    s[i] = "0"
                elif has_left_option:
                    s[i] = "L"
                    is_changed = True
                elif has_right_option:
                    s[i] = "R"
                    is_changed = True
                else:
                    # Not forced in any direction, but do not have any options
                    return False
        if not has_empty:
            return True
        if not is_changed:
            return None

def try_and_fix(s):
    result = fix(s)
    printf(s)
    if result != None:
        return result
    else:
        for i in range(2, n + 2):
            if s[i] == "0":
                s_copy = s.copy()
                s_copy[i] = "L"
                print(f"Trying L at {i - 2}:")
                printf(s_copy)
                result = try_and_fix(s_copy)
                if result:
                    return True
                else:
                    s_copy[i] = "R"
                    print(f"Trying R at {i - 2}:")
                    printf(s_copy)
                    result = try_and_fix(s_copy)
                    return result

t = int(input())
for tt in range(t):
    n = int(input())
    s = input()

    s = list("BB" + s + "BB")
    
    print(try_and_fix(s))
