def test_glsl(self) -> None:
    layout(binding = 0) buffer Pos {
        uint values[ ];
    };

    layout (local_size_x = 1, local_size_y = 1, local_size_z = 1) in;

    layout (constant_id = 0) const uint BUFFER_ELEMENTS = 32;

    uint fibonacci(uint n) {
	    if(n <= 1){
		    return n;
	    }
	    uint curr = 1;
	    uint prev = 1;
	    for(uint i = 2; i < n; ++i) {
		    uint temp = curr;
		    curr += prev;
		    prev = temp;
	    }
	    return curr;
    }

    void main()
    {
	    uint index = gl_GlobalInvocationID.x;
    	if (index >= BUFFER_ELEMENTS)
		    return;
	    values[index] = fibonacci(values[index]);
    }
