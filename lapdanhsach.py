import streamlit as st
class vao_viec:
    def _init_(self,df):
        self.df=df
    def function1(self,df):
        st.write('Giới tính')
        col1, col2 = st.columns([1,1])
        with col1:
            check1=st.checkbox('Nam')
        with col2:
            check2=st.checkbox('Nữ')
        page_name=['Lớp 10','Lớp 11','Lớp 12','Lớp buổi sáng','Lớp buổi chiều']
        page=st.radio('Các Lớp học',page_name)
        if page=='Lớp 10':
            hs_10=df[df['CLASS'].str.contains('10')]
            if check1:
                hs_10_nam=hs_10[hs_10['GENDER'].str.contains('M')]
                if check1 and check2:
                    st.write(hs_10)
                else:
                    st.write(hs_10_nam)
            elif check2:
                hs_10_nu=hs_10[hs_10['GENDER'].str.contains('F')]          
                st.write(hs_10_nu)
            else:
                st.write(hs_10)
        elif page=='Lớp 11':
            hs_11=df[df['CLASS'].str.contains('11')]
            if check1:
                hs_11_nam=hs_11[hs_11['GENDER'].str.contains('M')]
                if check1 and check2:  
                    st.write(hs_11)
                else:
                    st.write(hs_11_nam)
            elif check2:
                hs_11_nu=hs_11[hs_11['GENDER'].str.contains('F')]
                st.write(hs_11_nu)
            else:
                st.write(hs_11)
        elif page=='Lớp 12':
            hs_12=df[df['CLASS'].str.contains('12')]
            if check1:
                hs_12_nam=hs_12[hs_12['GENDER'].str.contains('M')]
                if check1 and check2:
                    st.write(hs_12)
                else:
                    st.write(hs_12_nam)
            elif check2:
                hs_12_nu=hs_12[hs_12['GENDER'].str.contains('F')]
                st.write(hs_12_nu)
            else:
                st.write(hs_12)
        elif page=='Lớp buổi sáng':
            hs_sang=df[df['PYTHON-CLASS'].str.contains('S')]
            if check1:
                hs_nam_sang=hs_sang[hs_sang['GENDER'].str.contains('M')]
                if check1 and check2:
                    st.write(hs_sang)
                else:
                    st.write(hs_nam_sang)
            elif check2:
                hs_nu_sang=hs_sang[hs_sang['GENDER'].str.contains('F')]
                st.write(hs_nu_sang)
            else:
                st.write(hs_sang)
        elif page=='Lớp buổi chiều':
            hs_chieu=df[df['PYTHON-CLASS'].str.contains('C')]
            if check1:
                hs_nam_chieu=hs_chieu[hs_chieu['GENDER'].str.contains('M')]
                if check1 and check2:
                    st.write(hs_chieu)
                else:
                    st.write(hs_nam_chieu)
            elif check2:
                hs_nu_chieu=hs_chieu[hs_chieu['GENDER'].str.contains('F')]
        
                st.write(hs_nu_chieu)
            else:
                st.write(hs_chieu)
        
            
               
        
            
       