def ecan_idxEntryToHeader(idx, entry):
    return (idx << 5) + entry

def ecan_hedaerToIdxEntry(header):
    idx = (header >> 5)
    entry = (header & 0b00011111)

    return idx, entry

def ecan_codeIdToAddr(unitCode, unitId, ism):
    ret = (unitCode << 5)
    ret += (unitId & 0b1111) << 1
    ret += ism

    return ret

def ecan_addrToCodeId(addr):
    unitCode = (addr >> 5)
    unitId = (addr & 0b00000011110) >> 1
    ism = addr & 0b00000000001

    return unitCode, unitId, ism

