class Vygenerovka:
    def __init__(self):
        self._text = ""
        self._klic = ""
        self._abeceda = "abcdefghijklmnopqrstuvwxyz"
        self._vysledek = ""
        self._mode = 0

    def __str__(self):
        return self._vysledek

    # def text_clean(self, var):
    #     special_symbols = ",.-§()+:-/*\"''$&@„?”!\n"
    #     new_text = ""

    #     for i in range(0, len(var)):
    #         if var[i] not in special_symbols:
    #             new_text += var[i]
    #         elif var[i] == "\n":
    #             new_text == " "
    #     return new_text

    # Funkce čistí text k šifrování od znaků, které nejsou v abecedě (CZ/ANG)
    def text_whitelist(self, var):
        new_text = ""
        
        for i in range(0, len(var)):
            if var[i] in self._abeceda:
                new_text += var[i]

        return new_text

    # Metoda, jenž obstárává interaktivní menu pro uživatele programu
    def menu(self):
        abeceda_tf = "n" 

        print("[1] Šifrovat pomocí Vygenerovy šifry")
        print("[2] Dešifrovat pomocí Vygenerovy šifry\n")

        self._mode = int(input("Zadejte volbu: "))

        if self._mode == 1:
            print("[1] Chcete provést šifrování textu s českou abecedou?")
            abeceda = input("y/n: ")
            
            if abeceda.lower() == "y":
                self._abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž "

            self.sifrovani()
        elif self._mode == 2:
            print("[1] Chcete provést dešifrování textu s českou abecedou?")
            abeceda = input("y/n: ")
            
            if abeceda.lower() "y":
                self._abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž "
            self.desifrovani()

    # def choose_alphabet(self) -> str:
    #     sepcial_letters = "čďňřšťžáéíóúýůě"
    #     if any(pismeno in self._text for pismeno in sepcial_letters):
    #         self._abeceda = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž "
    #     else:
    #         self._abeceda = "abcdefghijklmnopqrstuvwxyz "

    # Funkce, která hledá pozici daného písmenka ze de/šifrovaného textu v dané abecedě a tuto pozici pak následně vrací do funkce sifrovani
    def get_position_in_alpha(self, text_atr :str) -> int:
        for i in range(0, len(text_atr)):
            for j in range(0, len(self._abeceda)):
                if text_atr[i] == self._abeceda[j]:
                    print("pozice:",j, "char:", self._abeceda[j]) 
                    return j

    # ...
    def sifrovani(self) -> str:

        if self._mode == 1:
            self._klic = input("Zadejte klíč: ").lower()
            self._text = input("Zadejte text k šifrování: ").lower()
        
        self._text = self.text_whitelist(self._text)
        print(self._text)

        text_pos = 0
        key_pos = 0
        new_word = ""
        for i in range(0, len(self._text)):

            if self._mode == 1:
                print("opakovani:", i)
                new_position = self.get_position_in_alpha(list(self._text)[text_pos]) + self.get_position_in_alpha(list(self._klic)[key_pos])
            else:
                new_position = self.get_position_in_alpha(list(self._text)[text_pos]) - self.get_position_in_alpha(list(self._klic)[key_pos])
            #print("keypos:", key_pos)
            #if new_position > 25:
            #    new_position = new_position-26
            if (len(self._abeceda) > 30):
                new_position = new_position % len(self._abeceda)
            else:
                new_position = new_position % len(self._abeceda)
            print("new_position:", new_position)

            new_letter = self._abeceda[new_position]
            #print("new_letter:",new_letter)

            self._vysledek += new_letter
            
            # pozice v textu akt a v klici akt
            text_pos += 1
            key_pos += 1

            if key_pos == len(self._klic):
                key_pos = 0

        print(self._vysledek)

    # je to jen taková pomocná metoda, která vlastně celou svou práci udělá reversně ve funkci sifrovani
    def desifrovani(self):
        self._klic = input("Zadejte klíč k dešifrování: ").lower()
        self._text = input("Zadejte text k dešifrování: ").lower()
        self.sifrovani()

        return self._vysledek

sifra = Vygenerovka()
#print(sifra.sifrovani())
#print(sifra.desifrovani())

sifra.menu()
