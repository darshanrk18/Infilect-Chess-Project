# Chess project

## How to run?

Be in the root directory => Open a command prompt / Terminal => Run "docker-compose up --build"

## How to test?

You can test the endpoint on postman. Below are the few test cases to test the endpoint:

### Test Case 1:

#### Request:

```curl
POST http://127.0.0.1:8000/chess/knight
```

#### Request Body:

```json
{
  "positions": {
    "Queen": "E7",
    "Bishop": "B7",
    "Rook": "G5",
    "Knight": "C3"
  }
}
```

#### Output:

```json
{ "valid_moves": ["B1", "A4", "D1", "A2"] }
```

### Test Case 2:

#### Request:

```curl
POST http://127.0.0.1:8000/chess/queen
```

#### Request Body:

```json
{
  "positions": {
    "Queen": "H1",
    "Bishop": "B7",
    "Rook": "H8",
    "Knight": "F2"
  }
}
```

#### Output:

```json
{ "valid_moves": ["B1", "C1", "B7", "G1", "A1", "H8", "E1", "F1"] }
```

### Test Case 3:

#### Request:

```curl
POST http://127.0.0.1:8000/chess/rook
```

#### Request Body:

```json
{
  "positions": {
    "Queen": "A5",
    "Bishop": "G8",
    "Rook": "H5",
    "Knight": "G4"
  }
}
```

#### Output:

```json
{
  "valid_moves": ["A5", "H1", "H4", "H3", "H8"]
}
```
