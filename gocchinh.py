import pandas as pd
import plotly.express as px
import streamlit as st
df=pd.read_csv('py4ai-score.csv')
df['BONUS'].fillna(0, inplace=True)
df['S1'].fillna(0, inplace=True)
df['S2'].fillna(0, inplace=True)
df['S3'].fillna(0, inplace=True)
df['S4'].fillna(0, inplace=True)
df['S5'].fillna(0, inplace=True)
df['S6'].fillna(0, inplace=True)
df['S7'].fillna(0, inplace=True)
df['S8'].fillna(0, inplace=True)
df['S9'].fillna(0, inplace=True)
df['S10'].fillna(0, inplace=True)
df['REG-MC4AI'].fillna('N',inplace=True)
from module_pseu import tao_lap
module_1=tao_lap()
phan_lop=module_1.phan_lop
dau_rot=module_1.dau_rot
df['CLASS-GROUP']=df.apply(phan_lop,axis=1)
df['ĐẬU/RỚT']=df.apply(dau_rot,axis=1)
from lapdanhsach import vao_viec
from vebieudo import ve
COLS = df.columns.values.tolist().copy()
def main():
    st.title('PHÂN TÍCH DỮ LIỆU LỚP PY4AI')
    tab1,tab2,tab3=st.tabs(['Danh sách học sinh','Phân bố và tỉ lệ ','Tra cứu điểm cá nhân'])
    with tab1:
        bat_dau_thoi=vao_viec()
        bat_dau_thoi.function1(df)
    with tab2:
        draw=ve()
        draw.phan_bo(df)  
    with tab3:
        st.write('***Chú ý:*** _Viết liền nhau, viết chữ thường và không dấu_')
        st.write('***Ví dụ:*** nguyenminhkhang, chautuannguyen')
        ten=st.text_input('')
        button=st.button('Tra cứu')
        if button:
            st.write(df[df['NAME']==ten])
            
      
                    
                    
            
         
            


        
main()


