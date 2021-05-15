# homomorphic-searching-scheme
## RDBMS IA-1 IA-2
<hr />
Name: Aditya Tawade <br/>
Class: SY COMP B <br/>
Roll No: 1911126 <br/>
Resarch Paper: A Homomorphic Searching Scheme For Sensitive Data In NoSQL Database <br/>
<hr /><br/>

### Steps to run the code

1. Clone the repository <br/>
  ```markdown
   git clone https://github.com/adityatawade12/homomorphic-searching-scheme.git 
  ```

2. Install the required packages <br/>
```markdown
pip install pymongo phe 
```

3. The program uses MongoDB for storing data. Start the MongoDB server if not already running.

4. The database of name 'newDb' has the required collections. Collection 'coll1' contains the private key and public key for encryption. Collection 'textData' holds the data which is stored and read. 

5. Go to the cloned directory <br/>
```markdown 
   cd homomorphic-searching-scheme
   ```

6. Run the main.py file <br/>
```markdown 
python main.py
```

7. To create a new record choose option 1, enter values to be stored as prompted

   ![image](https://user-images.githubusercontent.com/62465343/118370850-496e0b00-b5c7-11eb-9e2d-2d4298f97ce8.png) <br/>

8. To search for a record stored in the database, choose option 2. Enter the value to be searched <br/>
    ![image](https://user-images.githubusercontent.com/62465343/118370882-702c4180-b5c7-11eb-9068-7d58e67a6b57.png)<br/>

9. To exit, choose option 3<br/>
    ![image](https://user-images.githubusercontent.com/62465343/118370908-918d2d80-b5c7-11eb-820a-6e9066511787.png)<br/>
 

------------

