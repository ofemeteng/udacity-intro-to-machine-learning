## PCA
changing n_components to the following values: [10, 15, 25, 50, 100, 250] produces the results below.
Exercise looks at F1 score for Ariel Sharon.
n_components = 10
                   precision    recall  f1-score   support

     Ariel Sharon       0.21      0.38      0.27        13
     Colin Powell       0.41      0.33      0.37        60
  Donald Rumsfeld       0.29      0.37      0.32        27
    George W Bush       0.64      0.62      0.63       146
Gerhard Schroeder       0.10      0.12      0.11        25
      Hugo Chavez       0.10      0.13      0.11        15
       Tony Blair       0.30      0.19      0.24        36

      avg / total       0.45      0.43      0.43       322

n_components = 15
                   precision    recall  f1-score   support

     Ariel Sharon       0.39      0.54      0.45        13
     Colin Powell       0.63      0.65      0.64        60
  Donald Rumsfeld       0.58      0.56      0.57        27
    George W Bush       0.76      0.77      0.76       146
Gerhard Schroeder       0.38      0.40      0.39        25
      Hugo Chavez       0.40      0.40      0.40        15
       Tony Blair       0.43      0.33      0.38        36

      avg / total       0.62      0.62      0.62       322

n_components = 25
                   precision    recall  f1-score   support

     Ariel Sharon       0.62      0.77      0.69        13
     Colin Powell       0.67      0.77      0.71        60
  Donald Rumsfeld       0.59      0.59      0.59        27
    George W Bush       0.82      0.82      0.82       146
Gerhard Schroeder       0.53      0.36      0.43        25
      Hugo Chavez       0.76      0.87      0.81        15
       Tony Blair       0.66      0.53      0.58        36

      avg / total       0.72      0.72      0.72       322

n_components = 50
                   precision    recall  f1-score   support

     Ariel Sharon       0.65      0.85      0.73        13
     Colin Powell       0.83      0.82      0.82        60
  Donald Rumsfeld       0.83      0.74      0.78        27
    George W Bush       0.86      0.90      0.88       146
Gerhard Schroeder       0.70      0.64      0.67        25
      Hugo Chavez       0.76      0.87      0.81        15
       Tony Blair       0.80      0.67      0.73        36

      avg / total       0.82      0.82      0.82       322

n_components = 100
                   precision    recall  f1-score   support

     Ariel Sharon       0.86      0.92      0.89        13
     Colin Powell       0.80      0.85      0.82        60
  Donald Rumsfeld       0.88      0.78      0.82        27
    George W Bush       0.87      0.90      0.89       146
Gerhard Schroeder       0.86      0.72      0.78        25
      Hugo Chavez       0.88      0.93      0.90        15
       Tony Blair       0.84      0.75      0.79        36

      avg / total       0.85      0.85      0.85       322

n_components = 250
                   precision    recall  f1-score   support

     Ariel Sharon       0.67      0.92      0.77        13
     Colin Powell       0.75      0.85      0.80        60
  Donald Rumsfeld       0.62      0.67      0.64        27
    George W Bush       0.88      0.86      0.87       146
Gerhard Schroeder       0.86      0.72      0.78        25
      Hugo Chavez       0.85      0.73      0.79        15
       Tony Blair       0.81      0.69      0.75        36

      avg / total       0.81      0.81      0.81       322