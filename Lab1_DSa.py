import arcpy

def buffer(layer, dist):
    # distance units should be in feet
    units = " feet"

    # combining the user input distance and the units, this is to be used in the arcpy.Buffer_analysis
    dist = dist + units

    #Output location path for the buffered layer
    output_layer = r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.gdb\\" + layer + "_buff"

    # Buffer analysis tool (input variable name, output variable name, distance type string,"FULL", "ROUND", "ALL")
    arcpy.Buffer_analysis(layer, output_layer, dist, "FULL", "ROUND", "ALL")

    print("Buffer created " + output_layer)
    return output_layer

# Takes the 4 buffer layers and prompts the user for an output layer name. It then performs the intersect and saves
# results to the westnilevirusoutbreak.gdb

def intersect(inter_list):
    # print the list being passed in
    print(inter_list)

    # ask the user to define an output intersect layer and store the results in a variable
    output_layer = input("Define the output intersect layer name:  ")

    # run a intersect analysis between the two buffer layer name and store the result in a variable
    # using arcpy.Intersect_analysis
    arcpy.Intersect_analysis(inter_list, output_layer)

    # print statement confirming intersect
    print("Intersect has been completed")

    # return the name of the new output layer
    return


def main():
    # get the project path and store it in a variable called aprx
    aprx = arcpy.mp.ArcGISProject(r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.aprx")

    # use a for loop to print out the map names within the project
    for map in aprx.listMaps():
        print("Map: " + map.name)

        # use a for loop to print the names of the layers within each map
        for lyr in map.listLayers():
            print("-" + lyr.name)


    # A container with a list of layer file names to be used in the buffer function
    LayerList = ["MosquitoLarvalSites","Wetlands","OSMPProperties","LakesandReservoirs"]
    print("These four layers will be buffered: ")
    print(LayerList)


    # Define workspace
    resultsgeodatabase = r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.gdb"
    arcpy.env.workspace = resultsgeodatabase

    # Checking the features in the geodatabase
    featureclasses = arcpy.ListFeatureClasses()
    print(arcpy.ListFeatureClasses())


    #Arcpy Function set to true, allows the old files to be overwritten by new ones.
    arcpy.env.overwriteOutput = True


    #Loop through the list of layers in variable name Layer_List and ask user for the buffer distance of each layer
    #to use as parameters for the buffer function (paramaters are layer and dist (short for distance))
    for layer in LayerList:
        print(layer)

        # ask user to define the buffer distance for each layer
        dist = input("Type in buffer distance(between 1000-5000 feet): ")

        # call buffer function, parameters passed are layer name and user input's distance in feet

        bufferlayer = buffer(layer, dist)

    #Check featureclasses in the geodatabase to confirm the 4 buffer layers were created
    featureclasses = arcpy.ListFeatureClasses()
    print(arcpy.ListFeatureClasses())

    #List of buffered layers used as a parameter for the intersect function
    inter_list = ["MosquitoLarvalSites_buff", "Wetlands_buff", "OSMPProperties_buff", "LakesandReservoirs_buff"]
    #intersect function called and parameter inter_listed passed. It then stores result in the variable
    #output_intersectlayer.
    output_intersectlayer = intersect(inter_list)

    #Check featureclasses in the geodatabase to confirm the intersect layer has been created
    featureclasses = arcpy.ListFeatureClasses()
    print(arcpy.ListFeatureClasses())

    #Arcpy Spatial Join, target feature, join_feature, out_feature_class
    target_feature = r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.gdb\BoulderAddresses"
    join_feature = r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.gdb\allinter"
    spatialjoin_name = input("Define the output spatial layer name: ")
    outfeature_sj = r"E:\GIS\GIS305\Lab1\Lab1\Lab1\Lab1.gdb\\" + spatialjoin_name

    output_spatialjoinlayer = arcpy.SpatialJoin_analysis(target_feature, join_feature, outfeature_sj)

    #Check featureclasses in the geodatabase to confirm the spatial join
    featureclasses = arcpy.ListFeatureClasses()
    print(arcpy.ListFeatureClasses())

    print("All Analysis is done! Go style the layers in Arc")






main()

