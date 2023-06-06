# TSP GLPK Resolver

## input model:

`public/inst_10.txt` example

`i` = number of entries <br>
`x & y` = coordinates of "city" <br>
`t` = service time <br>
`d` = (deadline)

```
 # [i]
 10
 # [x] [y] [t] [d]
 27  45
  5  96   9 430
  4  87   7  17
 67   5   8 449
 77 100  20 490
 96  24  11 428
 78  68  17 535
 91  64   6  28
 15  26   7 419
```

The file must keep this pattern. If you change it you will have to change the `read_data` function in the `read_data.py` file.

Please, see the public files for more examples.

# Usage

### install deps:

```bash
pip install numpy pymprog flask flask-cors
```

# How to run

### flask api

```bash
flask --app main run
```

### cache generator

some file examples are in the`./public/` folder. But you can use any file.

The TSP issue needs a lot of time to resolve. To provide data in Flask API faster we can run the model and store data in a JSON file.

When the user makes a request, API send a cached JSON file. The cache can disable with `cache: false` in the request body.

```bash
python generate-cache.py ./public/inst_10.txt
```
