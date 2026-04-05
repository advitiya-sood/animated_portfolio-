declare module "gsap-trial/SplitText" {
  export class SplitText {
    constructor(target: any, vars: any);
    revert(): void;
    chars: any[];
    words: any[];
    lines: any[];
  }
}

declare module "gsap-trial/ScrollSmoother" {
  export class ScrollSmoother {
    static create(vars: any): ScrollSmoother;
    paused(value: boolean): void;
    scrollTop(): number;
    scrollTo(target: any, smooth?: boolean, position?: string): void;
    kill(): void;
  }
}
