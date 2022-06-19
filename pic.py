import sys, fitz
import os
import datetime
 
def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()
    
    print("imagePath="+imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        
        if not os.path.exists(imagePath):
            os.makedirs(imagePath) 
        
        pix.writePNG(imagePath+'/'+'images_%s.png' % pg)
        
    endTime_pdf2img = datetime.datetime.now()
    print('times=',(endTime_pdf2img - startTime_pdf2img).seconds)
 
 

