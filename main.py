
AA={
'ALA':'A','ARG':'R',
'ASN':'N','ASP':'D',
'CYS':'C','GLN':'Q',
'GLU':'E','GLY':'G',
'HIS':'H','ILE':'I',
'LEU':'L','LYS':'K',
'MET':'M','PHE':'F',
'PRO':'P','SER':'S',
'THR':'T','TRP':'W',
'TYR':'Y','VAL':'V'
}
def list_to_string(list):
    strings= ''
    for element in list:
        strings= strings + element
    return strings
PDB='7AY1'
f = open("7AY1.pdb")
list_aa=[]#每一条链的AA
list_Sequence=[]#所有链的序列以string按次序存入
list_chain=['A']#链
# num=0

while 1:
    lines=f.readlines(100000)
    if not lines:
        break
    for line in lines:
        if(line[0]=='A'and line[1]=='T'and line[2]=='O'and line[3]=='M'):
            if(line[21]!=list_chain[-1]):
                # print(line[21] +" " +" " + list_chain[-1])
                # print(num)
                list_chain.append(line[21])
                list_Sequence.append(list_to_string(list_aa))
                list_aa.clear()
            if(line[13]=='N'and line[14]==' '):
                str_aa = line[17] + line[18] + line[19]
                aa=AA[str_aa]
                list_aa.append(aa)
        # num += 1
list_Sequence.append(list_to_string(list_aa))

f.close()
fasta = open("test.fasta", "w")
for i in range(len(list_Sequence)):
    line_a='>' + PDB +'_' + str(i+1) + '|chain ' + list_chain[i] + '\n'
    fasta.writelines('>' + PDB +'_' + str(i+1) + '|chain ' + list_chain[i] + '\n')

    fasta.writelines(list_Sequence[i]+'\n')

fasta.close()
