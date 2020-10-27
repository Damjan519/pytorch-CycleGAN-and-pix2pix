Spine T9
3D ultrasound (US) volume --> T9_IM_0087_frame1 (NII file) 
3D MRI volume --> 96_96_80_T9_CROP_NII_MR_ (NII file) [this crop based on whole_spine_MR]

Spine T1-T12
3D MRI volume --> whole_spine_MR.nii (NII file) aka NIFTI file format
              --> WholeSpineCleanDIC.dcm (DCM file)
              --> WholeSpineClean_NII.nii (DICOM to NII conversion of WholeSpineCleanDIC.dcm)

powerpoint slide --> GAN_dataset_TEST
                 --> goes over the volumes mentioned above, cropping in the 'z direction', 
                 and a tool (MRIcron) to view these volumes

    ### MR volume separated into each vertebra ###
'To see where each vertebra and intervertebral disc is located in the MRI volumes, check the slides
GAN_dataset_TEST.pptx'
    ##############################################

    ### Viewing/Analyzing 3D NII volumes ###
'please see the slides mentioned above to see a example of a tool used to view the volumes we will be working with.
I believe this viewer only works with NIFTI files. 

This is just a suggestion, you can use whatever you want. If you find a better viewer or better way to do the cropping (python code below)
please use whatever suits you. These are just examples and suggestions i provided.'
    ########################################

----PYTHON CODE---------

    ### Converting a directory with dicom files to nifti files ### 
'This is just for completeness and probably wont be required, but if you want to try it out there is
    this version and the one in the slides mentioned above'
    
import dicom2nifti # link to available documentation/help --> https://github.com/icometrix/dicom2nifti
dicom2nifti.convert_directory(dicom_directory, output_folder, compression=True, reorient=True)
    ##############################################################

    ### Cropping (can be done in one direction or all directions [x,y,z] ) done on NIFTI files  ###
import nibabel as nib
import os
outdir = 'path to output directory'
image = 'path to .nii file'
img = nib.load(image)
cropped = img.slicer[98:194, 25:121, 234:314]  #size becomes [96,96,80]
cropped.to_filename(os.path.join(outdir, str(96)+"_"+str(96)+"_"+str(80)+"_"+ "T4_CROP_NII_MR_.nii.gz"))

                     #EXAMPLE#
 ##size of whole_spine_MR [0:270 , 0:128 , 0:384]
 ##size of WholeSpineClean [0:96 , 0:70 , 0:337]
image = 'C:/Users/Damjan/Desktop/MRI_US_Image_Registration/TESTING_DATASET/MR_nii/whole_spine_MR.nii'
img = nib.load(image)
#MR original size [0:270,0:128,0:384]
# 13- 81 --> 303-371 (68 pixels) , 17-81 --> 303-367
# T4 70-150 --> (384-150) 234, (384-70)
cropped = img.slicer[98:194, 25:121, 234:314]  #size becomes [96,96,80]
outdir = 'C:/Users/Damjan/Desktop/MRI_US_Image_Registration/TESTING_DATASET/MR_nii'
cropped.to_filename(os.path.join(outdir, str(96)+"_"+str(96)+"_"+str(80)+"_"+ "T4_CROP_NII_MR_.nii.gz"))
    ################################################################################################

  ### plot a specific 'frame' or 2D image contained within the volume ###
import matplotlib.pyplot as plt
import numpy as np
check = np.load('C:/Users/Damjan/Desktop/MRI_US_Image_Registration/TESTING_DATASET/MR_nii/cropMR_norm.npz')['vol_data']
plt.imshow(check[:,:,3]) # 2D image corresponding to frame 3
  #######################################################################
