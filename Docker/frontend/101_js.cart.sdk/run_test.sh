kubectl exec -it `kubectl get pods|grep "js-cart-sdk-" |cut -c1-28` -- bash -c "cd /js.cart.sdk/ ;npm run test-ci"