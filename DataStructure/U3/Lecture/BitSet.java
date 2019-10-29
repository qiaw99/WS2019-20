public class BitSet
{
    int maxvalue;
    long A[];

    BitSet(int maxv) {
	maxvalue = maxv;
	int size = 1+maxv/64;
	A = new long[size];
    }

    public boolean contains(int i) {
	if ((i>maxvalue)||(i<0)) return false;
	int k = i/64;
	int shift = i-k*64;
	return ((A[k]>>shift) & 1)==1;
    }
    
    public void add(int i)
    {
    }


    public void remove(int i)
    {
    }




}
