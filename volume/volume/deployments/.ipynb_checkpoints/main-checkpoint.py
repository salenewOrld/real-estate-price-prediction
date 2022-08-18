from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    id : str
    mssubclass : str
    mszoing : str
    lotarea : str
    street : str
    alley : str
    lotshape : str
    landcontour : str
    utilities : str
    lotconfig: str
    landslope : str
    neighborhood : str
    condition1 : str
    condition2 : str
    bldgtype : str
    housestyle : str
    overallqual : str
    overallcond : str
    yearbuilt : int
    yearremodadd : int
    roofstyle : str
    roofmatl : str
    exterior1st : str
    exterior2nd : str
    masvnrtype : str
    masvnrarea : str
    exterqual : str
    extercond : str
    foundation : str
    bsmtqual : str
    bsmtcond : str
    bsmtexposure : str
    bsmtfintype1 : str
    bsmtfinsf1 : str
    bsmtfintype2 : str
    bsmtunfsf : str
    totalbsmtsf : str
    heating : str
    heatingqc : str
    centralair : str
    electrical : str
    firstflrsf : str
    secondflrsf : str
    lowqualfinsf : str
    grlivarea : str
    bsmtfullbath : str
    bsmthalfbath : str
    fullbath : str
    halfbath : str
    bedroomabvgr : str
    kitchenabvgr : str
    kitchenqual : str
    totrmsabvgrd : str
    functional : str
    fireplaces: str
    fireplacequ : str
    garagetype: str
    garageyrblt : str
    garagefinish: str
    garagecars: str
    garagearea : str
    garagequal : str
    garagecond : str
    paveddrive : str
    wooddecksf : str
    openporchsf : str
    enclosedporch : str
    threessnporch : str
    screenporch : str
    poolarea : str
    poolqc : str
    fence : str
    miscfeature : str
    miscval : str
    mosold : str
    yrsold : str
    saletype : str
    salecondition : str
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/get_predicted_price')
async def get_predicted_price(data : Item):
    predicted_value = 'Test'
    return {'Message' : {'predicted_value' : predicted_value}}