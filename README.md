# RESTLess
We open source the prototype of RESTLess in this repositories. RESTLess is  a generic framework for improving the efficiency of REST API Fuzzing. More details will be there soon. 
## services,specification
The services and specification directories contain the images of the services selected for testing in this thesis and their corresponding openapi documentation.
## tools
The tools directory contains the implementation projects for all the comparison tools selected for this thesis.
## render_order_opt.py
The render_order_opt is used to divide the openapi document into essential and non-essential parameters. When the fuzzer fills in the parameters, it first picks the essential parameters to fill in to ensure that the request sequence is as long as it can be.
Then the non-essential parameters are probabilistically filled. In this way, in order to ensure the length of the original request sequence, by filling the non-essential parameter values to further expand the test case space. The code in the file is the main code of the parameter filling process, and the request sequence is constructed by referring to resttestgen.
The request sequence is constructed with reference to resttestgen and other mainstream REST API fuzz tools, for more details, please refer to their corresponding projects in the tools directory.
## extract.py
The extract file extracts the parameter-parameter values from the successful response of the fuzz tool, which can be used for subsequent LLM model training. In order to train the test parameter values that match the semantic information of the parameters.
## llm-spec-ennhenced.py
Utilizes the gpt-3.5 model to train recommended parameter values that conform to the semantic information of the parameter through the hints project for subsequent openapi document enhancement and ultimately for the parameter generation process.
## format.py
The format file is used to format the parameters and the trained parameter values in the llm-spec-ennhenced.py file, storing the parameters and parameter values in a dictionary for subsequent processing.
## format_file.json
format_file.json shows the results of the format.py file, i.e. the trained parameters and their values. Used to enhance API documentation
## merged.py
Adds the trained parameter values to the openapi documentation in the form of an 'enum' field, enhancing the subsequent parameter generation process.

For some commercial reasons, we are unable to disclose all the source code at this time. We welcome readers who are interested in restless to communicate with us at zhengtao20@stu.scu.edu.cn, chenxsh@scu.edu.cn; we also welcome readers to come to Sichuan University to meet us face-to-face. Address: Multidisciplinary Building, Sichuan University, Chuanda Road, Shuangliu District, Chengdu, Sichuan, China. We promise to publish a runnable version as well as related data and code as soon as possible.
