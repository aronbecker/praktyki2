export class Validator {
    private validators: { [key: string]: (str: string) => boolean } = {};
    private values: { [key: string]: () => string } = {};
    private correct: { [key: string]: boolean } = {};

    addField(
        id: string,
        val: () => string,
        validationFunc: (str: string) => boolean
    ) {
        this.validators[id] = validationFunc;
        this.values[id] = val;
        this.correct[id] = false;
    }

    addEmailField(id: string, val: () => string) {
        this.addField(id, val, (str: string) => {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(str);
        });
    }

    private validate() {
        for (const [key, value] of Object.entries(this.values)) {
            this.correct[key] = this.validators[key](value());
        }
    }

    isValid() {
        this.validate();
        return Object.values(this.correct).every(
            (value) => value === true
        );
    }
}
