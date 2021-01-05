import os

if __name__ == "__main__":
    path = os.path.join(os.getcwd(),"Daily_Files")
    for i in range(1,366):
        day = str.zfill(str(i),3)
        file_name = "Day_{}.md".format(day)
        file_path = os.path.join(path,file_name)
        if not os.path.isfile(file_path):
            try:
                with open(file_path,"x") as f:
                    f.write("# Day {} of ML ".format(str(i)))
                    f.write("\n\n\n")
                    f.write("**References**\n------------\n[1]  \n[2]")
                    f.close()
            except:
                print("Failed in creating markdown file for day {}".format(day))
        else:
            print("Skipped")
