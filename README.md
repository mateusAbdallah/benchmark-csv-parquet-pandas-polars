 - Benchmarking of time taken to write and read csv and parquet file.
    - CSV 
        - CSV dataframe 1x
            - Size: 28.7MB

        - CSV dataframe 10x
            - Size: 328.3MB

        - CSV dataframe 100X
            - Size: 3.3GB
    - Parquet
        - Parquet dataframe 1x
            - Size: 10.2MB

        - Parquet dataframe 10x
            - Size: 95.4MB

        - Parquet dataframe 100x
            - Size: 951.7MB

 The objective of this repository is to measure the time consumption taken to write and read CSV and parquet files. The size of the original dataset does increase 10x and 100x. Above are the size of each file.

  To measure the time is used timeit python's module
  To visualize the charts is used streamlit module.

  