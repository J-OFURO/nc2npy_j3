c nc2bin_j3
c
c sample_02.f
c
c reading npy 
c----------------------------------------------------------------------- 
      parameter(ix=1440,jy=720,lt=12, iskip=20)
      real*4 dat(ix*jy*lt),dat3d(ix,jy,lt)

      open(50,file="J-OFURO3_NHF_MONTHLY_HR_2002.npy"
     &       ,form="unformatted",access="stream")

      read(50) (dat(n),n=1,ix*jy*lt+skip)

c reshape
      n=1+iskip
      do l=1,lt
       do j=1,jy
        do i=1,ix
         dat3d(i,j,l)=dat(n) 
         n=n+1
        enddo
       enddo
      enddo

c check output
       i=720
       j=360
       do l=1,12
        write(6,*) l,dat3d(i,j,l)
       enddo

      stop
      end
