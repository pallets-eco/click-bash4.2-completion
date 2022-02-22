# click-bash4.2-completion
Bash 4.2 completion support for Click 8.0.x

Beginning with Click 8.0.x, completion support for older Bash versions was dropped. See https://github.com/pallets/click/issues/2152 and https://github.com/pallets/click/issues/2200

This package adds support for Bash version 4.2

## Usage
```python
from click_bash42_completion import patch

patch()

... your click code ...

```
