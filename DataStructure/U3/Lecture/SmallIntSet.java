class SmallIntSet
{
    static int maxsize=100;
    int m;
    int A[];

    SmallIntSet()
    {
	m = 0;
	A = new int[maxsize];
    }

    public boolean add(int i) throws RuntimeException
    {
	for (int j=0; j<m; j++)
	    {
		if (A[j]==i) return false;
	    }
	if (m==maxsize)
	    throw new RuntimeException();
            // oder eine spezifischere Ausnahme
	A[m] = i;
	m = m+1;
	return true;
    }


    public boolean remove(int i)
    {
	for (int j=0; j<m; j++)  {
	    if (A[j]==i) {
		for (int k=j+1; k<m; k++)
		    A[k-1]=A[k];
		m = m-1;
		return true;
	    }
	}
	return false;
    }


    public boolean contains(int i)
    {
	for (int j=0; j<m; j++)  {
	    if (A[j]==i) return true;
	}
	return false;
    }


}
