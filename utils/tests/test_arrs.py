from utils.arrs import get , my_slice

spisok = ["artem","Edem","Maksim"]
spisok2 = ["Кни́га","один","видов","печатной","продукции"]

def test_get():
   assert get(spisok,2,0) == "Maksim"
   assert get(spisok,0,1) == "artem"

def test_my_slice():
   assert my_slice(spisok2,0,1) == ["Кни́га"]
   assert my_slice(spisok2,0,3) == ['Кни́га', 'один', 'видов']