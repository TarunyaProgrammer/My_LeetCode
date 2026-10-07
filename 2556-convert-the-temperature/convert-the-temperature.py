class Solution:
    def convertTemperature(self, cel: float) -> List[float]:
        def kel(cel):return cel + 273.15
        def far(cel):return cel * 1.80 + 32.00
        return [kel(cel),far(cel)]