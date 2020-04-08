import wpf
import clr
clr.AddReference('System')
#clr.AddReference('System.Drawing')

from System.Windows import Application, Window
from Microsoft.Win32 import OpenFileDialog
from System.Windows.Media.Imaging import BitmapImage
from System.Windows.Media import LinearGradientBrush, GradientStop, Colors
from System import Uri
#from System.Drawing.Drawing2D import LinearGradientBrush
#from System.Drawing import Point, Color

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'RetinaSegmentation.xaml')
    
    def BtnBrowse_Click(self, sender, e):
        try:
            dlgOrg = OpenFileDialog()
            dlgOrg.Title = "Select orginal picture"
            dlgOrg.DefaultExt = ".jpg"
            dlgOrg.Filter = "JPG|*.jpg|PNG|*.png|TIF|*.tif"

            dlgMask = OpenFileDialog()
            dlgMask.Title = "Select mask picture"
            dlgMask.DefaultExt = ".tif"
            dlgOrg.Filter = "JPG|*.jpg|PNG|*.png|TIF|*.tif"

            if dlgOrg.ShowDialog(self):
                if dlgMask.ShowDialog(self):
                    print(dlgOrg.FileName)
                    print(dlgMask.FileName)
                    self.img.Source = BitmapImage(Uri(dlgOrg.FileName))
                    self.imgResult.Source = BitmapImage(Uri(dlgMask.FileName))
                    #import Test
        except e:
            print("Error: {}", e)
        return 0

    def lbImgs_SelectionChanged(self, sender, e):
        index = self.lbImgs.SelectedIndex
        print(index)       
        path = "G:\\Projects\\Bachelor Project\\RetinaSegmentation\\RetinaSegmentation\\DataSet\\"

        self.rbGradable.IsChecked = True
        if index == 0:
            self.rbGrade0_Normal.IsChecked = True
            self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_37.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                
            
            self.rbNotGradable.IsChecked = True
            self.img.Source = BitmapImage(Uri(path + "Grade0_Normal.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "Grade0_Normal.jpg"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False

        elif index == 1:
            self.rbIDRiD_32.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_37.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_32.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_32_EX.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHardExudates.IsChecked = True

        elif index == 2:
            self.rbIDRiD_35.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_37.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False

            self.img.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_35.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_35_EX.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHardExudates.IsChecked = True

        elif index == 3:
            self.rbIDRiD_37.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_37.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HardEx\\IDRiD_37_EX.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHardExudates.IsChecked = True

        elif index == 4:
            self.rbHEIDRiD_04.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "HE\\IDRiD_04.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HE\\IDRiD_04_HE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHemorrhage.IsChecked = True

        elif index == 5:
            self.rbIDRiD_06.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "HE\\IDRiD_06.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HE\\IDRiD_06_HE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHemorrhage.IsChecked = True

        elif index == 6:
            self.rbIDRiD_08.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "HE\\IDRiD_08.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "HE\\IDRiD_08_HE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbHemorrhage.IsChecked = True

        elif index == 7:
            self.rbMAIDRiD_04.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "MA\\IDRiD_04.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "MA\\IDRiD_04_MA.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbMicroaneurysm.IsChecked = True

        elif index == 8:
            self.rbIDRiD_24.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "MA\\IDRiD_24.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "MA\\IDRiD_24_MA.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbMicroaneurysm.IsChecked = True

        elif index == 9:
            self.rbIDRiD_44.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "MA\\IDRiD_44.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "MA\\IDRiD_44_MA.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbMicroaneurysm.IsChecked = True

        elif index == 10:
            self.rbIDRiD_31.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_31.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_31_SE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbSoftExudates.IsChecked = True

        elif index == 11:
            self.rbSEIDRiD_32.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_35.IsChecked = False                

            self.img.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_32.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_32_SE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbSoftExudates.IsChecked = True

        elif index == 12:
            self.rbSEIDRiD_35.IsChecked = True
            self.rbGrade0_Normal.IsChecked = self.rbIDRiD_37.IsChecked = self.rbHEIDRiD_04.IsChecked = self.rbIDRiD_06.IsChecked = self.rbIDRiD_08.IsChecked = self.rbIDRiD_24.IsChecked = self.rbIDRiD_31.IsChecked = self.rbIDRiD_32.IsChecked = self.rbIDRiD_35.IsChecked = self.rbIDRiD_44.IsChecked = self.rbMAIDRiD_04.IsChecked = self.rbSEIDRiD_32.IsChecked = False

            self.img.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_35.jpg"))
            self.imgResult.Source = BitmapImage(Uri(path + "SoftEx\\IDRiD_35_SE.tif"))
            self.cbHemorrhage.IsChecked = self.cbMicroaneurysm.IsChecked = self.cbSoftExudates.IsChecked = self.cbHardExudates.IsChecked = False
            self.cbSoftExudates.IsChecked = True

        self.Recommended()

    def Recommended(self):
        if self.cbHardExudates.IsChecked == True or self.cbHemorrhage.IsChecked == True or self.cbMicroaneurysm.IsChecked == True or self.cbSoftExudates.IsChecked == True:
            
            myBrush = LinearGradientBrush()
            myBrush.GradientStops.Add(GradientStop(Colors.Yellow, 0.0))
            myBrush.GradientStops.Add(GradientStop(Colors.Orange, 0.5))
            myBrush.GradientStops.Add(GradientStop(Colors.Red, 1.0))
            self.lblRecommended.Background = myBrush
            self.lblRecommended.Content = "Recommended Refer"
            
        else:
            myBrush = LinearGradientBrush()
            myBrush.GradientStops.Add(GradientStop(Colors.Green, 0.0))
            myBrush.GradientStops.Add(GradientStop(Colors.LawnGreen, 0.5))
            myBrush.GradientStops.Add(GradientStop(Colors.DarkGreen, 1.0))
            self.lblRecommended.Background = myBrush
            self.lblRecommended.Content = "Recommended No Refer"


if __name__ == '__main__':
    Application().Run(MyWindow())