{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2cd75ce7-4e85-4943-b2b8-28f4a832a375",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9fefdb66-81a4-4eab-acdf-839d806b641b",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=joblib.load(\"../models/linear_regression.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "02544d5e-f6a8-4f4b-99c0-b3b4ffd53155",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted Score: 77.39580248031388\n"
     ]
    }
   ],
   "source": [
    "sample = pd.DataFrame({\n",
    "    \"Hours Studied\":[7],\n",
    "    \"Previous Scores\":[85],\n",
    "    \"Extracurricular Activities\":[1],\n",
    "    \"Sleep Hours\":[7],\n",
    "    \"Sample Question Papers Practiced\":[5]\n",
    "})\n",
    "prediction=model.predict(sample)\n",
    "print(f\"Predicted Score: {prediction[0]}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d0d8bc8-9111-45e8-a574-b4ba4dcf66db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
