#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:48:30 2020
@author: RitikaRamprasad
"""


import math
import pandas as pd
from shapely.geometry.polygon import Polygon
from ccdc.descriptors import CrystalDescriptors
from ccdc.io import EntryReader
from ccdc.io import MoleculeReader
import numpy as np

df = pd.read_csv('match_results_TPbi.csv')

df_id = df.iloc[:,2]
csd_mol_reader = MoleculeReader('CSD')


mol = pd.Series([csd_mol_reader.molecule(df_id[i]) for i in range(len(df_id.head(200)))])
mol_smile = pd.Series([mol[i].smiles for i in range(len(mol))])
mol_smiles = pd.DataFrame(mol_smile.values.tolist(), index = mol_smile.index, columns = ['Smile ID'])
df = pd.merge(df, mol_smiles, right_index=True, left_index=True)
df.to_excel('TPbi_Smiles.xlsx')
