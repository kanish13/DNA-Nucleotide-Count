import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

img =Image.open("dna.jpg")

with st.columns(5)[1]:
        st.image(img,width=400,)

st.write("""

<h1 style='text-align:center;'>DNA NUCLEOTIDE COUNT WEB APP</h1>
        
<h4 style="text-align:center;">This app counts the nucleotide of query DNA!!!</h4>

        """, unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

st.header("Enter the DNA sequence")



seq=st.text_area("Sequence Input",height=250)

if seq:
    seq=seq.splitlines()

    seq=seq[1:]

    seq="".join(seq)

    st.write('''
    ***
            ''')

    st.header("Input (DNA Query)")

    seq

    st.write('''
    ***
            ''')


    st.header("OUTPUT (DNA Nucleotide Count)")

    def DNA_N_C(seq):
        d={
            'A':seq.count('a'),
            'T':seq.count('t'),
            'G':seq.count('g'),
            'C':seq.count('c')
        }
        return d

    x=DNA_N_C(seq)


    st.write("There are "+str(x["A"])+" Adenine (A)")
    st.write("There are "+str(x["T"])+" Thymine (T)")
    st.write("There are "+str(x["G"])+" Guanine (G)")
    st.write("There are "+str(x["C"])+" Cytosine (C)")

    st.write('''
    ***
            ''')


    df=pd.DataFrame(list(x.items()),columns=["Nucleotide","Count"])

    df

    st.write('''
    ***
            ''')

    p=alt.Chart(df).mark_bar().encode(
        x="Nucleotide",
        y="Count"
    )
    p=p.properties(width=alt.Step(80))

    st.write(p)