// pipe function to resolve func1(func2(func3(vars))) to pipe(func1, func2, func3)(vars)
export const pipe = (...funcs) => {
  return async function (val) {
    for (let func of funcs) {
      val = await func(val);
    }
    return val;
  };
};
