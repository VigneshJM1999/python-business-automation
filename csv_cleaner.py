def main():
    input_file = 'sales_raw.csv'
    output_file = 'sales_clean.csv'

    output_lines = []

    new_header = "product_id,quantity,sale_price,order_date,total_price\n"
    output_lines.append(new_header)

    try:
        with open(input_file, 'r') as f:
            all_lines = f.readlines()

            for line in all_lines[1:]:

                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')

                product_id = parts[0].strip()
                quantity_str = parts[1].strip()
                price_str = parts[2].strip()
                order_date = parts[3].strip()

                if not product_id:
                    continue

                if not quantity_str:
                    continue

                product_id = product_id.upper()

                price_str = price_str.replace('$', '').replace(' ', '')

                try:
                    quantity_val = int(quantity_str)
                    price_val = float(price_str)

                    total_price = quantity_val * price_val

                except ValueError:
                    print(f"Skipping bad row: {line}")
                    continue

                new_line = f"{product_id},{quantity_val},{price_val},{order_date},{total_price}\n"

                output_lines.append(new_line)

        with open(output_file, 'w') as f_out:
            f_out.writelines(output_lines)

        print(f"Cleaning complete. Wrote {len(output_lines) - 1} data rows to {output_file}.")

    except FileNotFoundError:
        print(f"Error: {input_file} not found. Make sure it's in the same folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()