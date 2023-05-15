import plotly.express as px
import streamlit as st
class ve:
    def _init_(self,df):
        self.df=df
    def phan_bo(self,df):
        page_name=['Điểm thi','Đậu và rớt','Đăng kí tiếp']
        page=st.radio('Biểu đồ phân tích',page_name)
        if page=='Điểm thi':
            fig=px.box(df,x='CLASS-GROUP',y='S6',color='GENDER')
            fig2=px.box(df,x='CLASS-GROUP',y='S10',color='GENDER')
            st.title('***Phân bố điểm thi giữa kì của lớp PY4AI***')
            st.plotly_chart(fig,use_container_width=True)
            st.title('***Phân bố điểm thi cuối kì của lớp PY4AI***')
            st.plotly_chart(fig2,use_container_width=True)
        elif page=='Đậu và rớt':
            tren_liet=df[df['GPA']>=6.0]
            duoi_liet=df[df['GPA']<6.0]
            fig=px.box(tren_liet,x='CLASS-GROUP',y='GPA',color='GENDER')
            fig2=px.pie(tren_liet,names='GENDER')
            fig3=px.pie(df,names='ĐẬU/RỚT')
            fig4=px.pie(duoi_liet,names='CLASS-GROUP')
            st.title('***Tỉ lệ học sinh đậu và rớt của lớp PY4AI***')
            st.plotly_chart(fig3,use_container_width=True)
            st.title('***Phân bố số học sinh đậu lớp PY4AI theo nhóm lớp và giới tính***')
            st.plotly_chart(fig,use_container_width=True)
            st.title('***Tỉ lệ đậu lớp PY4AI giữa nam và nữ***')
            st.plotly_chart(fig2,use_container_width=True)
            st.title('***Tỉ lệ học sinh rớt của lớp PY4AI theo nhóm lớp***')
            st.plotly_chart(fig4,use_container_width=True)
        elif page=='Đăng kí tiếp':
            dang_ki=df[df['REG-MC4AI']=='Y']
            fig=px.histogram(dang_ki,x='CLASS-GROUP',color='GENDER')
            fig2=px.pie(df,names='REG-MC4AI')
            st.title('***Tỉ lệ học sinh đăng kí và không đăng kí tiếp lớp MC4AI***')
            st.plotly_chart(fig2,use_container_width=True)
            st.title('***Phân bố số lượng học sinh đăng kí tiếp lớp MC4AI theo giới tính và nhóm lớp***')
            st.plotly_chart(fig,use_container_width=True)    