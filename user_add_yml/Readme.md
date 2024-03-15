### User Creation YAML Generator

This Python script facilitates the creation of YAML files for Ansible, enabling the configuration of user settings based on user input. It prompts users to provide details such as usernames, email addresses, shell preferences, and group memberships. The script securely generates passwords and logs user inputs for record-keeping.

#### Usage

1. Run the script.
2. Follow the prompts to input user details.
3. YAML files with user configurations will be generated for Ansible.

#### Requirements

- Python 2.7 or higher
- Cryptography library (for password generation)

#### Usage Example

```bash
python user_creation_script.py
