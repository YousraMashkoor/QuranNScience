import { INTERVAL, ATTEMPTS_LEFT } from "../constants";

const componentLoader = (
  lazyComponent,
  attemptsLeft = ATTEMPTS_LEFT,
  interval = INTERVAL
) => {
  return new Promise((resolve, reject) => {
    lazyComponent()
      .then(resolve)
      .catch((error) => {
        setTimeout(() => {
          if (attemptsLeft === 1) {
            console.log("Lazy Loading Error: ", error);
            reject(error);
            return;
          }
          componentLoader(lazyComponent, attemptsLeft - 1, interval).then(
            resolve,
            reject
          );
        }, interval);
      });
  });
};

export default componentLoader;
