class tao_lap:
    def _init_(self,row):
        self.row=row
    def phan_lop(self,row):
        if row['CLASS'][2]=='C':
            if row['CLASS'][3]=='V':
                return 'Chuyên Văn'
            elif row['CLASS'][3]=='T':
                if row['CLASS'][3:]=='TIN':
                    return 'Chuyên Tin'
                elif row['CLASS'][3:]=='TRN':
                    return ' Trung Nhật'
                else:
                    return 'Chuyên Toán'
            elif row['CLASS'][3]=='L':
                return 'Chuyên Lý'
            elif row['CLASS'][3]=='H':
                return 'Chuyên Hóa'
            elif row['CLASS'][3]=='A':
                return 'Chuyên Anh'
            elif row['CLASS'][3:]=='SD':
                return 'Sử Địa'
        elif row['CLASS'][2:4]=='TH':
            return 'Tích hợp'
        elif row['CLASS'][2:4]=='SN':
            return 'Song Ngữ'
        else:
            return 'Không chuyên'
    def dau_rot(self,row):
        if row['GPA']>=6.0:
            return 'Đậu'
        else:
            return 'Rớt'
    
   
        
    

