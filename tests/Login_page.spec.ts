import { test, expect } from '@playwright/test';

test('Login Page', async ({ page }) => {
  await page.goto('https://practice.expandtesting.com/login');
  await expect(page.getByRole('heading', { name: 'Test Login page for' })).toBeVisible();
  await page.getByRole('textbox', { name: 'Username' }).fill('Practice');
  await page.getByRole('textbox', { name: 'Password' }).fill('SuperSecretPassword!');

  await page.getByRole('button', { name: 'Login' }).click();
  await expect(page.getByText('You logged into a secure area!')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Hi, practice!' })).toBeVisible();
  await page.getByRole('link', { name: 'Logout' }).click();
  await page.getByRole('textbox', { name: 'Username' }).click();
  await page.getByRole('textbox', { name: 'Username' }).fill('admin');
  await page.getByRole('textbox', { name: 'Username' }).press('Tab');
  await page.getByRole('textbox', { name: 'Password' }).fill('admin');
  await page.getByRole('button', { name: 'Login' }).click();
  await expect(page.getByText('Your password is invalid!')).toBeVisible();
});