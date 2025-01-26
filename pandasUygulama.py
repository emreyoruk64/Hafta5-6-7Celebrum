import pandas as pd
import numpy as np
data=[[25,5000],[30,6000],[22,4500],[27,5200]]
dataFrame=np.array(data)
yeniDataFrame=pd.DataFrame(data,index=["Veli","Ayşe","Mehmet","Betül"],columns=["Yaş","Maaş"])
ortMaas=yeniDataFrame["Maaş"].mean()
ortYas=yeniDataFrame["Yaş"].mean()
print(yeniDataFrame[yeniDataFrame["Maaş"]>5000])
print(yeniDataFrame)
print(ortMaas)
print(ortYas)
print(yeniDataFrame["Yaş"].sort_values())