weight, goal_pred, input , alpha= {0.5, 0.8, 2, 0.4}

for iteration in range(20):
    print("-----\nWeight:" + str(weight))
    pred = input * weight
    error = (pred-goal_pred) ** 2
    delta = pred - goal_pred
    derivative = input * delta
    weight = weight - (alpha * derivative)

    print("Error:" + str(error) + " Prediction:" + str(pred))
    print("Delta:" + str(delta) + " Derivative:" + str(derivative))