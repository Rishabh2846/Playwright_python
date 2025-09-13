import { test, expect } from '@playwright/test';

test('API testing using UI', async ({ page }) => {
  await page.goto('https://practice.expandtesting.com/notes/api/api-docs/');
  await page.getByRole('button', { name: 'GET /health-check Check the' }).click();
  await page.getByRole('button', { name: 'Try it out' }).click();
  await page.getByRole('button', { name: 'Execute' }).click();
  await expect(page.getByRole('table').getByRole('code').getByText('200')).toBeVisible();
  await expect(page.getByText('"Notes API is Running"')).toBeVisible();
  await page.getByRole('button', { name: 'POST /users/register Creates' }).click();
  await page.getByRole('button', { name: 'Try it out' }).click();
  await page.getByRole('textbox', { name: 'name' }).click();
  await page.getByRole('textbox', { name: 'name' }).fill('admin');
  await page.getByRole('textbox', { name: 'name' }).press('Tab');
  await page.getByRole('textbox', { name: 'email' }).fill('admin@test.com');
  await page.getByRole('textbox', { name: 'password' }).click();
  await page.getByRole('textbox', { name: 'password' }).fill('admin');
  await page.locator('#operations-Users-post_users_register').getByRole('button', { name: 'Execute' }).click();
  await page.getByRole('textbox', { name: 'password' }).click();
  await page.getByRole('textbox', { name: 'password' }).fill('admin4567');
  await page.locator('#operations-Users-post_users_register').getByRole('button', { name: 'Execute' }).click();
await expect(page.getByText('"An account already exists')).toBeVisible();

await page.getByRole('button', { name: 'POST /users/login Log in as' }).click();
await page.getByRole('button', { name: 'Try it out' }).click();
await page.getByRole('cell', { name: 'User email' }).getByPlaceholder('email').click();
await page.getByRole('cell', { name: 'User email' }).getByPlaceholder('email').fill('admin@test.cpm');
await page.getByRole('cell', { name: 'User email' }).getByPlaceholder('email').press('Tab');
await page.getByRole('cell', { name: 'User email admin@test.cpm' }).getByPlaceholder('email').click();
await page.getByRole('cell', { name: 'User email admin@test.cpm' }).getByPlaceholder('email').fill('admin@test.com');
await page.getByRole('cell', { name: 'User password' }).getByPlaceholder('password').click();
await page.getByRole('cell', { name: 'User password' }).getByPlaceholder('password').fill('admin4567');
await page.locator('#operations-Users-post_users_login').getByRole('button', { name: 'Execute' }).click();
await expect(page.locator('#operations-Users-post_users_login').getByText('200').nth(1)).toBeVisible();
await expect(page.getByText('"admin"')).toBeVisible();
await expect(page.getByText('"admin@test.com"')).toBeVisible();

});