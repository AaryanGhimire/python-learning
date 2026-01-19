#usied to store data values in "key":value pairs
#they are unordered ,mutable(changeable)&dont allow multiple keys
info=  {
    
    "name":"aaryan",
    "topic":33
}
print(info)
print(type(info))
print(info["name"])
info["name"]="Haaland"#changes name in info dictionary ie overwrite
print(info)

null_dict ={}
null_dict["name"]="Cherki"
print(null_dict)
#null dictionary can be used in various cases and added data afterwards