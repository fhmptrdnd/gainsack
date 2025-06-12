from my_heap import build_heap, heappop

def heap_sort_proposal(proposals, key, ascending=True):
    heap = [(proposal[key], i, proposal) for i, proposal in enumerate(proposals)]

    build_heap(heap, ascending=ascending)

    sorted_proposals = []
    while heap:
        _, _, proposal = heappop(heap, ascending=ascending)
        sorted_proposals.append(proposal)

    return sorted_proposals

def cari_proposal(proposals, nama_perusahaan):
    return [p for p in proposals if nama_perusahaan.lower() in p["NAMA PERUSAHAAN"].lower()]

def knapsack_proposal(proposals, modal_investor):
    proposal_rasio = []
    for proposal in proposals:
        biaya_original = proposal["BIAYA AWAL"]
        laba_original = proposal["TOTAL LABA INVESTOR"]
        biaya = biaya_original / 1000000
        laba = laba_original / 1000000
        rasio = laba / biaya if biaya > 0 else float('-inf') 
        proposal_rasio.append({'rasio': rasio, 'original_proposal': proposal})
    
    sorted_proposal_rasio = heap_sort_proposal(proposal_rasio, key='rasio', ascending=False)
    
    laba_maks = 0
    proposal_diambil = []
    sisa_modal = modal_investor

    for item in sorted_proposal_rasio:
        proposal = item['original_proposal']
        biaya = proposal["BIAYA AWAL"]
        laba = proposal["TOTAL LABA INVESTOR"]
        
        if biaya <= sisa_modal:
            laba_maks += laba
            proposal_diambil.append(proposal)
            sisa_modal -= biaya
    
    return laba_maks, proposal_diambil