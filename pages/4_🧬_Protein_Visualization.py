from stmol import *
import streamlit as st
import py3Dmol

st.set_page_config(page_title="Protein Visualization Demo", page_icon="🧬")

st.markdown("# Protein Visualization Demo")
st.sidebar.header("Protein Visualization Demo")
st.write(
    """This demo illustrates protein visualization using the stmol component (https://github.com/napoles-uach/stmol). """
)

# col1, col2 = st.columns(2)

# with col1:
st.write('This is the structure of thrombin inhibited by AERUGINOSIN298-A from a BLUE-GREEN ALGA. The PDB ID is 1A2C.')

    # with st.empty():
xyzview = py3Dmol.view(query='pdb:1A2C') 
xyzview.setStyle({'cartoon':{'color':'spectrum'}})
showmol(xyzview, height = 500,width=800)

# with col2:
st.write(
    """You can label residues of your choice in the protein, like so."""
)

showmol(render_pdb_resn(viewer = render_pdb(id = '1A2C'),resn_lst = ['ALA', 'ARG']))