# parking plane to empty gate# < gate_max, return True if parking is successful
def parking_plane(gates, plane, gate_max):
    for g in range(gate_max, 0, -1):
        if gates[g] == 0:
            gates[g] = plane
            return True

    return False


def max_planes(limits, gates):  #O(GP) solution
    for plane_num, gate_limit in enumerate(limits, 1):
        if not parking_plane(gates, plane_num, gate_limit):
            print(plane_num - 1)
            return
    
    print(len(limits))


G = int(input())
P = int(input())
limits = [int(input()) for _ in range(P)]
gates = [0] * (G + 1)

max_planes(limits, gates)
