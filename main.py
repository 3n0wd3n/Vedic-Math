class Math:

    def __init__(self, first_number, second_number):
        self.fnumber = first_number
        self.snumber = second_number
        self.fnum_arr = []
        self.snum_arr = []
  
    def get_fnumber(self):
        return self.fnumber
  
    def get_snumber(self):
        return self.snumber
  
    def set_fnumber(self, fnumber):
        self.fnumber = fnumber
        return self
  
    def set_snumber(self, snumber):
        self.snumber = snumber
        return self

    def get_fnum_arr(self):
        return self.fnum_arr

    def set_fnum_arr(self, arr):
        self.fnum_arr = arr
        return self

    def get_snum_arr(self):
        return self.snum_arr

    def set_snum_arr(self, arr):
        self.snum_arr = arr
        return self

    def fnumber_to_arr(self):
        fnum = self.get_fnumber()
        fnum = str(fnum)
        arr = list(fnum)
        self.set_fnum_arr(arr)
        return self

    def snumber_to_arr(self):
        snum = self.get_snumber()
        snum = str(snum)
        arr = list(snum)
        self.set_snum_arr(arr)
        return self

    def get_len_of_fnum_arr(self):
        return len(self.get_fnum_arr())

    def get_len_of_snum_arr(self):
        return len(self.get_snum_arr())

    def check_same_lenght(self):
        return self.get_len_of_fnum_arr() == self.get_len_of_snum_arr()

    def which_longer(self):
        if self.get_len_of_fnum_arr() > self.get_len_of_snum_arr():
          return "first one"
        return "second one"

    def fill_with_zero(self):
        if self.get_len_of_fnum_arr() == 0 or self.get_len_of_snum_arr() == 0:
          return "I can not work with zeros"
        len_of_fnum = self.get_len_of_fnum_arr()
        len_of_snum = self.get_len_of_snum_arr()
        if self.which_longer() == "first one":
          difference = len_of_fnum - len_of_snum
          for i in range(difference):
            tmp_arr = self.get_snum_arr()
            tmp_arr = ["0"] + tmp_arr
            self.set_snum_arr(tmp_arr)
        else:
          difference = len_of_snum - len_of_fnum
          for i in range(difference):
            tmp_arr = self.get_fnum_arr()
            tmp_arr = ["0"] + tmp_arr
            self.set_fnum_arr(tmp_arr)
        return self

    def get_order(self):
        if not self.check_same_lenght():
          return "not same order"
        return self.get_len_of_fnum_arr()

    def multiplication(self):
        order = self.get_order()
        if not order == "not same order":
          if order == 2:
            fnum_arr = self.get_fnum_arr()
            snum_arr = self.get_snum_arr()
            store = ""
            result = ""
            for i in range(3, 0, -1):
              if i == 3:
                fnum = int(fnum_arr[1])
                snum = int(snum_arr[1])
                tmp_result = fnum * snum
                tmp_result = list(str(tmp_result))
                if len(tmp_result) > 1:
                  store = "".join(tmp_result[0:len(tmp_result)-1])
                  tmp_result = tmp_result[len(tmp_result)-1:]
                  result = tmp_result[0] + result
                else:
                  result = tmp_result[0] + result
              if i == 2:
                fnum_1 = int(fnum_arr[1])
                fnum_0 = int(fnum_arr[0])
                snum_1 = int(snum_arr[1])
                snum_0 = int(snum_arr[0])
                if store:
                  tmp_result = fnum_1 * snum_0 + fnum_0 * snum_1 + int(store)
                else:
                  tmp_result = fnum_1 * snum_0 + fnum_0 * snum_1
                tmp_result = list(str(tmp_result))
                if len(tmp_result) > 1:
                  store = "".join(tmp_result[0:len(tmp_result)-1])
                  tmp_result = tmp_result[len(tmp_result)-1:]
                  result = tmp_result[0] + result
                else:
                  result = tmp_result[0] + result
              if i == 1:
                fnum = int(fnum_arr[0])
                snum = int(snum_arr[0])
                if store:
                  tmp_result = fnum * snum + int(store)
                else:
                  tmp_result = fnum * snum
                tmp_result = str(tmp_result)
                result = tmp_result + result
          return result      
        return "can not apply method multiplication --> not same order"
  
m = Math(2, 88)
print("Get fnumber", m.get_fnumber())
print("Get snumber", m.get_snumber())
print("Setting fnumber")
m.set_fnumber(76)
print("Get fnumber", m.get_fnumber())
print("Get fnumber array", m.get_fnum_arr())
print("Get snumber array", m.get_snum_arr())
print("Setting fnumber array and snumber array")
m.fnumber_to_arr()
m.snumber_to_arr()
print("Get fnumber array", m.get_fnum_arr())
print("Get snumber array", m.get_snum_arr())
print("Checking if they are same lenghth =", m.check_same_lenght())
print("Checking which is longer =", m.which_longer())
print("Filling with zero")
m.fill_with_zero()
print("Get fnumber array", m.get_fnum_arr())
print("Get snumber array", m.get_snum_arr())
print("Checking if they are same lenghth =", m.check_same_lenght())
#print("Multiplication of " + str(m.get_fnumber()) + " and " + str(m.get_snumber()) + " acording to VEDIC MATHS is", m.multiplication())
print("Multiplication of {0} and {1} according to Vedic Math is {2}." .format(m.get_fnumber(), m.get_snumber(), m.multiplication()))
        
    
  
    
        

