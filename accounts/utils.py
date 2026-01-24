from .utils import Mahsulot
class Mahsulot:
    def __init__(self, nomi, narxi, uzunligi):
        self.nomi = nomi
        self.narxi = narxi
        self.uzunligi = uzunligi

    def turi(self, turi):
        return f"Turi: {turi}"

    def get_info(self):
        return f"Nomi: {self.nomi}, Narxi: {self.narxi}, Uzunligi: {self.uzunligi}"

    def set_price(self, yangi_narxi):
        self.narxi = yangi_narxi
        return f"Yangi narxi: {self.narxi}"
        
class mahsulotlar:
    def __init__(self,nomi,narxi,uzunligi):
        self.nomi=nomi
        self.narxi=narxi
        self.uzunligi=uzunligi
    def turi(self,turi):
        self.turi=turi
        return (f"Turi: {self.turi}")
    def get_info(self):
        return (f"Nomi: {self.nomi}, Narxi: {self.narxi}, Uzunligi: {self.uzunligi}")
    def set_price(self,yangi_narxi):
        self.narxi=yangi_narxi
        return (f"Yangi narxi: {self.narxi}")