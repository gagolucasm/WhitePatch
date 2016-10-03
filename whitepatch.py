__author__ = 'lucasgago'

import cv2
import cv
import time
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
    start_time = time.time()
    ret, image = cap.read()
    image=np.asarray(image)
    cv2.imshow("LAFOTO",image)

    p=1.123

    B,G,R = cv2.split(image)
    """
    imager=cv2.merge([R*p,G*p,B*p])
    cv2.imshow("Alreves",imager)
    """


    """
    for i in range (0,y-1):
        for j in range (0,x-1):
            (b,g,r)=image[i,j]

            if r>maxr:
                maxr=r
            if g>maxg:
                maxg=g
            if b>maxb:
                maxb=b
    """

    print "Los valores maximos son:"
    #print maxr,maxb,maxg
    maxr=np.amax(R)
    maxb=np.amax(B)
    maxg=np.amax(G)
    print maxr,maxg,maxb

    sr=float(255)/maxr
    sg=float(255)/maxg
    sb=float(255)/maxb
    print "Los parametros de correcion son:"
    print sr,sg,sb
    """
    for i in range (0,y-1):
        for j in range (0,x-1):
            (b,g,r)=image2[i,j]
            image2[i,j]=(int(b*sb),int(g*sg),int(r*sr))
    """
    """
    R=R*sr
    G=G*sg
    B=B*sb
    """
    print "R 1 es"
    print R.shape
    """
    for x in range(719):
        for y in range(1279):
            R[x][y]=(int(R[x][y] * sr))
    for x in range(719):
        for y in range(1279):
            G[x][y]=(int(G[x][y] * sr))
    for x in range(719):
        for y in range(1279):
            B[x][y]=(int(B[x][y] * sr))
    """

    #R=[(int(x * sr)) for x in R]
    #G=[(int(x * sg)) for x in G]
    #B=[(int(x * sb)) for x in B]
    R=np.asarray(R)
    G=np.asarray(G)
    B=np.asarray(B)
    image22=cv2.merge([B,G,R])
    cv2.imshow("LAFOTOCORREGIDAs",image22)

    R=R.astype(int)
    G=G.astype(int)
    B=B.astype(int)

    print "el maximo de R es :"
    print np.mean(R)

    image2=cv2.merge([B,G,R])


    #(b,g,r)=image2[0,0]
    #print b,g,r

    cv2.imshow("LAFOTOCORREGIDA",image2)
    elapsed_time = time.time() - start_time
    print "EL tiempo que tarda es:"
    print elapsed_time
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()